$(init_page);

/////////////////////////////////////////////////////////////////////////////////////////////
function init_page()
{
    $('.set_url').click(save_url_handler);
    $('#myTab a').click(change_view);
    $('#actionCheck a').click(change_view_list);
    $('.parse_db').click(parse_handler);
    $('.search_a').click(search_handler);
    $(function () {
        $('#myTab a:first').tab('show');
    });
}
/////////////////////////////////////////////////////////////////////////////////////////////

function change_view(e)
{
    e.preventDefault();
    $(this).tab('show');
}
/////////////////////////////////////////////////////////////////////////////////////////////

function change_view_list()
{
    var index = $(this).parent().index();
    $(this).parents('ul').find('li').removeClass('active').andSelf().find('li').eq(index).addClass('active');
    $('.'+$(this).parents('ul').attr('id')).find('.tab_actions').hide().eq(index).show();
}
/////////////////////////////////////////////////////////////////////////////////////////////

function parse_handler()
{
	var data = true;
    $.get($('#parse_content_by_words').val()).done(function(response){
    	$('.alert-success').removeClass('none');
    	$('.parse_db').addClass('none');
        $('.alert-success').empty().append(response.message);
    }).fail(function() {
        console.log('This');
        return false;
    });
}
/////////////////////////////////////////////////////////////////////////////////////////////

function save_url_handler()
{
    $.post($('#set_url_on_db').val(),
            get_data_url()
    ).done(function(response){
        if(response)
        {
        	$('.badge-success').removeClass('none');
        }
    }).fail(function() {
        return false;
    });
}

function get_data_url()
{
	var result = {};
	result['name'] = $('#inputName').val();
	result['url'] = $('#inputUrl').val();
	return result;
}
/////////////////////////////////////////////////////////////////////////////////////////////

function generate_result(sitename, searchword, history) {
	return '<h4>Site name: '
        + sitename
        +'</h4><p>Search word: <span class="badge">'
        + searchword
        +'</span></p><p>Element history: <span class="label label-info">'
        + history
        +'</span></p>'
}

function search_handler()
{
    console.log('search_handler');
    $.get($('#find_need_word').val(), {"q": $('.search-query').val()}
    ).done(function(response){
        console.log(response);
        var result = '';
//            row-fluid marketing
        $.each(response, function(index, value)
        {
//            console.log(value.site_name, value.search_word, value.tag_history);
            result += generate_result(value.site_name, value.search_word, value.tag_history);
        });
        $('.results').empty().append(result);
    }).fail(function() {
        return false;
    });
}