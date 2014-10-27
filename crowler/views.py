# -*- coding: utf-8 -*-
import json
from datetime import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from crowler.tools.DBDataManager import CDBDataManager
from crowler.tools.HtmlParserManager import HtmlParseManager
from crowler.models import RelevantWords
from core.models import SiteConfig

def crowler_main(request):
    params = {}
    # params['error'] = 'Test'
    params['data'] = SiteConfig.objects.filter()
    return render_to_response('crowler/main.html',
                          params, context_instance = RequestContext(request))

@csrf_exempt
def set_url_on_db(request):
    reqParams = request.POST.dict()
    print reqParams
    result  = CDBDataManager(reqParams).saveUrl()
    return HttpResponse(json.dumps({'status':True, 'message':'Any error!'}), content_type = "application/json")

def parse_content_by_words(request):
    for el in SiteConfig.objects.filter():
        hPM = HtmlParseManager(el)
        hPM.make_list_of_words()
        hPM.save_words_to_db()
    return HttpResponse(json.dumps({'status': True,
                                    'message': u'Parse is already OK :-8'}),
                        content_type='application/json; charset=utf-8')

def find_need_word(request):
    objects = RelevantWords.objects.filter(word=request.GET.dict().get('q'))
    ret_list = []
    for obj in objects:
        some_dict = {
            'search_word': obj.word,
            'tag_history': obj.tag_history,
            'site_name': obj.siteConfig.name
        }
        ret_list.append(some_dict)
    return HttpResponse(json.dumps(ret_list),
                        content_type='application/json; charset=utf-8')

