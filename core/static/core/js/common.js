function getURLParameter(name) {
    return decodeURI(
        (RegExp(name + '=' + '(.+?)(&|$)').exec(location.search)||[,null])[1]
    );
}

function dispatch_exception(message)
{
	$.msgBox({
            title: "Error",
            content: message,
            type: "error",
            buttons: [{ value: "Ok" }]
        });
}

function reload()
{
	return window.location.reload(true);
}

function input_only_numbers($element)
{
	$element.keydown(function (event){
	    if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 
            || event.keyCode == 27 || event.keyCode == 13 
            || (event.keyCode == 65 && event.ctrlKey === true) 
            || (event.keyCode >= 35 && event.keyCode <= 39)){
                return;
        }else {
            if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault(); 
            }   
        }
	});

}

function input_only_float_numbers($element)
{
	$element.keydown(function (event){
		
	   if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 190
	        || event.keyCode == 27 || event.keyCode == 13 
	        || (event.keyCode == 65 && event.ctrlKey === true) 
	        || (event.keyCode >= 35 && event.keyCode <= 39)){
	            return;
	    }else {
	        if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
	            event.preventDefault(); 
	        }   
	    }
	});
	
}

function currency_format(amount)
{
	var i = parseFloat(amount);
	if(isNaN(i)) { i = 0.00; }
	var minus = '';
	if(i < 0) { minus = '-'; }
	i = Math.abs(i);
	i = parseInt((i + .005) * 100);
	i = i / 100;
	s = new String(i);
	s = s.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
	if(s.indexOf('.') < 0) { s += '.00'; }
	if(s.indexOf('.') == (s.length - 2)) { s += '0'; }
	s = minus + s;
	return s;
}

function toggle_ajax_loader(bool) {
	$('#ajax_loader').hide();
	if(bool) {
		$('#ajax_loader').show();
	}
}
