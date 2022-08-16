var sumation_data;
var table_state = {
    'category' : '전체',
    'page_num' : 0
};
function click_event_page(num){
    table_state['page_num'] = num;
    update_table();
}
function click_event_news(name){
    table_state['category'] = name;
    update_table();
}
// news table update
function update_table(){
    var category_state = table_state['category'];
    var data = sumation_data[category_state];
    
    var page_num = Math.ceil(data.length/10);
    var paging = $('div.page_button');

    var contents = $('ul.news_contents');
    var page_num_state = table_state['page_num'] * 10;

    $('div.page_button *').remove();
    $('ul.news_contents *').remove();

    for(var i = 0;i<page_num;i++){
        paging.append('<a href = "javascript:return false;" class = "page_num"' + `onclick = "click_event_page('${i}');" ` + '>' + (i + 1) + '</a>');
    }
    if (data.length - page_num_state < 10){
        temp = data.length - page_num_state;
    }
    else{
        temp = 10;
    }

    for(var i = 0;i<temp;i++){
        contents.append('<li class = "coin_news_items"><a id = "news_name" href = '
        + data[i + page_num_state][1] + '>'
        + data[i + page_num_state][0] +'</a></li>');
    }
}
// data scaling
function Sumation(data){
    var category_name = ['전체','일반','규제/정책','산업/테크','칼럼/인터뷰'];
    var news_dic = {};

    // create list
    for(var i = 0;i<category_name.length;i++){
        news_dic[category_name[i]] = []
    }

    // split data
    for(var i = 0;i<data.length;i++){
        line = [];
        line.push( data[i]['news_name'] );
        line.push( data[i]['news_href'] );
        news_dic[ data[i]['category'] ].push( line );
    }
    sumation_data = news_dic;
}

// logout
function logout(){
    sessionStorage.removeItem("user_id"); // keyName에 해당하는 값 삭제
    sessionStorage.removeItem("password"); // keyName에 해당하는 값 삭제
}
// data getering
$(document).ready(function(){
    var category_name = ['전체','일반','규제/정책','산업/테크','칼럼/인터뷰'];
    var numbers = $('#numbers');

    // add category label
    for(var i = 0;i<category_name.length;i++){
        numbers.append('<li><a href = "#" class = "TabLabel"'+ `onclick = "click_event_news('${category_name[i]}');" ` +'>' + category_name[i] +'</a></li>');
    }
    login_ck = $(".navbar_menu");
    seetion_user_id = sessionStorage.getItem("user_id")
    if (seetion_user_id != null){
        login_ck.append(`<li><a href = "../userpage">UserPage</a></li>`);
        login_ck.append(`<li><a href = "../home" onclick = "logout()" >Logout</a></li>`);
    }
    else{
        login_ck.append(`<li><a href = "../login">Login</a></li>`);
        login_ck.append(`<li><a href = "../sign_up">Register</a></li>`);
    }
    numbers.css({
        "display" : "flex",
    });
    $('#numbers li').css({
        "font-size" : "23px",
        "list-style" : "none",
    });
    $('a.TabLabel').css({
        "text-decoration" : "none",
        "color" : "white",
        "border" : "1px solid #263343",
        "padding-left" : "22px",
        "padding-right" : "22px",
        "padding-top" : "11px",
        "padding-bottom" : "11px",
        "background-color" : "#263343",
        "border-radius" : "7px",
        "margin-right" : "11px",
    });
    $.ajax({
        type : "GET",
        url : get_url,
        success : function(data){
            Sumation(data);
            update_table();
        }
    });
    
})