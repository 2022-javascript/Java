// logout
function logout(){
    sessionStorage.removeItem("user_id"); // keyName에 해당하는 값 삭제
    sessionStorage.removeItem("password"); // keyName에 해당하는 값 삭제
}
$(document).ready(function(){
    login_ck = $(".navbar_menu");
    seetion_user_id = sessionStorage.getItem("user_id")
    seetion_password = sessionStorage.getItem("password")
    if (seetion_user_id != null){
        login_ck.append(`<li><a href = "../userpage">UserPage</a></li>`);
        login_ck.append(`<li><a href = "../AIResearch">AI Research</a></li>`);
        login_ck.append(`<li><a href = "../home" onclick = "logout()" >Logout</a></li>`);
        login_ck.append(`<li><a href = "../trade">Trade</a></li>`);
    }
    else{
        login_ck.append(`<li><a href = "../login">Login</a></li>`);
        login_ck.append(`<li><a href = "../sign_up">Register</a></li>`);
    }
    $.ajax({
        type : "GET",
        url : get_url,
        success : function(data){
            var flag = 0,idx = 0;
            for(var i = 0;i<data.length;i++){
                if(data[i]['Email'] == seetion_user_id){
                    idx = i;
                    flag = 1;
                    break;
                }
            }
            if(flag != 1){
                console.log("데이터베이스에 일치하는 이메일이 없습니다.");
            }
            else{
                $.ajax({
                    type : "POST",
                    url : post_url,
                    data : {
                        "Api_key" : data[idx]['api_key'],
                        "Sec_key" : data[idx]['sec_key']
                    }
                });
            }
        },
        error : function(){
            console.log("error");
        }
    })
})