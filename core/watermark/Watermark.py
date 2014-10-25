# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2014

@author: oganin
'''
import urllib2
import os
import tempfile
from zipfile import ZipFile
from PIL import Image, ImageEnhance
from core.settings import CFG_PATH
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class CWatermark(object):
    def __init__(self, mark=CFG_PATH+"/watermark/press.png", padding=250):
        self._mark = mark
        self._padding = padding
    
    def reduce_opacity(self, img, opacity):   
        """Returns an image with reduced opacity."""
        
        assert opacity >= 0 and opacity <= 1
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        else:
            img = img.copy()
        alpha = img.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        img.putalpha(alpha)
        
        return img

    def watermark(self, img, position = 'bottom-right', opacity = 0.6):
        """Adds a watermark to an image."""
    
    #     img = Image.open(img)
        mark = Image.open(self._mark)
        img_w_p = img.size[0] - self._padding
        if img_w_p < mark.size[0]:
            ratio = float(img_w_p) / mark.size[0]
            w = int(mark.size[0] * ratio)
            h = int(mark.size[1] * ratio)
            mark = mark.resize((w, h))
        
        if opacity < 1:
            mark = self.reduce_opacity(mark, opacity)
        
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # create a transparent layer the size of the image and draw the watermark in that layer.
        layer = Image.new('RGBA', img.size, (0,0,0,0))
        
        if position == 'over':
            for y in xrange(0, img.size[1], mark.size[1]):
                for x in xrange(0, img.size[0], mark.size[0]):
                    layer.paste(mark, (x, y))
        elif position == 'title':
            # title, but preserve the aspect ratio
            ratio = min(float(img.size[0]) / mark.size[0], float(img.size[1]) / mark.size[1])
            w = int(mark.size[0] * ratio)
            h = int(mark.size[1] * ratio)
            mark = mark.resize((w, h))
            # layer.paste(mark, ((img.size[0] - w) / 2, (img.size[1] - h) / 2))
            layer.paste(mark, ((img.size[0] - w) / 2, 0))
        elif position == 'top-left':
            position = (self._padding, self._padding)
            layer.paste(mark, position)
        elif position == 'top-right':
            position = (img.size[0] - mark.size[0] - self._padding, self._padding)
            layer.paste(mark, position)
        elif position == 'center':
            position = ((img.size[0] - mark.size[0])/2, (img.size[1] - mark.size[1])/2)
            layer.paste(mark, position)
        elif position == 'bottom-left':
            position = (self._padding, img.size[1] - mark.size[1]  -self._padding,)
            layer.paste(mark, position)
        else: # 'bottom-right' (default)
            position = (img.size[0] - mark.size[0] - self._padding, img.size[1] - mark.size[1] - self._padding,)
            layer.paste(mark, position)
            
        return Image.composite(layer, img, layer)
    
    def imageOpen(self, img_url, response):
        urlData = urllib2.urlopen(img_url).read()
        tf = tempfile.NamedTemporaryFile(delete=True)
        tfName = tf.name
        tf.seek(0)
        tf.write(urlData)
        tf.flush()
        imageList = list()
        if self._getExtension(img_url) == 'zip':
            imageList = self._zipOpen(tfName)
        else:
            im = Image.open(tfName)
            if im.format == 'TIFF' or im.format == 'TIF':
                im = self._tiffopen(tfName)
            imageList.append(im)
        
        finalyImageList = list()
        for currentImage in imageList:
            finalyImageList.append(self.watermark(currentImage, 'top-right',opacity=0.8))
        
        return self.createPdf(finalyImageList, response)
       
    def _tiffopen(self, filename):
        os.system("tiffcp -c none %s temp.tif" % filename)
        im = Image.open("temp.tif")
        os.remove("temp.tif")
        return (im)
    
    def _getExtension(self, url):
        return str(url).split('/')[-1].split('?')[0].split('.')[-1]
    
    def _zipOpen(self, fileName):
        zf = ZipFile(fileName, 'r')
        imagelist = list()
        for currentFile in zf.filelist:
            tf = tempfile.NamedTemporaryFile(delete=True)
            tf.seek(0)
            tf.write(zf.read(currentFile.filename))
            tf.flush()
            im = Image.open(tf.name)
            imagelist.append(im)
        return imagelist
    
    def createPdf(self, ImageList, response):
        p = canvas.Canvas(response, pagesize=A4)
        for currentImage in ImageList:
            currentImage.thumbnail(A4, Image.ANTIALIAS)
            tf = tempfile.NamedTemporaryFile(delete=True)
            tf.flush()
            currentImage.save(tf.name, 'png')
            p.drawImage(tf.name, 1, 1)
            p.showPage()
        p.save()
        
        return response
    
    
    
        