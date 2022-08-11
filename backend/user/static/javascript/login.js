function LoginCk(){
    id = document.getElementById('id').value;
    password = document.getElementById('password').value;
    $.ajax({
        type : "GET",
        url : get_url,
        success : function(data){
            var flag = 0;
            for(var i = 0; i < data.length; i++){
                if(data[i]['user_id'] == id && data[i]['password'] == password){
                    flag = 1;
                    break;
                }
            }

            if(flag == 0){
                alert("아이디 또는 비밀번호를 잘못 입력했습니다.");
                window.location.href = "/login";
            }
            else{
                sessionStorage.setItem("user_id",id);
                sessionStorage.setItem("password",password);
                alert("로그인 되었습니다");
                window.location.href = "/home";
            }
        },
        error : function(){
            alert(get_url);
        }
    });
}
$(document).ready(function(){
    login_ck = $(".navbar_menu");
    seetion_user_id = sessionStorage.getItem("user_id")
    if (seetion_user_id != null){
        login_ck.append(`<li><a href = "../userpage">UserPage</a></li>`);
        
    }
    else{
        login_ck.append(`<li><a href = "../login">Login</a></li>`);
        login_ck.append(`<li><a href = "../sign_up">Register</a></li>`);
    }
});