$(init_page);

/////////////////////////////////////////////////////////////////////////////////////////////
function init_page()
{
    $('.set_url').click(save_url_handler);
    $('#myTab a').click(change_view);
    $('#actionCheck a').click(change_view_list);
    $('.parse_db').click(parse_handler);
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