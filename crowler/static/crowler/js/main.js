$(init_page);

/////////////////////////////////////////////////////////////////////////////////////////////
function init_page()
{
    $('.parse_db').click(save_url_handler);
    $('#myTab a').click(change_view);
    $('#actionCheck a').click(change_view_list);
    $(function () {
        $('#myTab a:first').tab('show');
    })
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

function save_url_handler()
{
    var data = true;
    $.post($('#set_url_on_db').val(),
            data
    ).done(function(response){
        console.log(response);
    }).fail(function() {
        console.log('This');
        return false;
    });

}
/////////////////////////////////////////////////////////////////////////////////////////////