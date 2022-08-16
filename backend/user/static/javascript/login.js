function LoginCk(){
    id = document.getElementById('id').value;
    password = document.getElementById('password').value;
    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2);
    var day = ('0' + today.getDate()).slice(-2);
    var dateString = year + '-' + month  + '-' + day;

    var hours = ('0' + today.getHours()).slice(-2); 
    var minutes = ('0' + today.getMinutes()).slice(-2);
    var seconds = ('0' + today.getSeconds()).slice(-2); 
    var timeString = hours + ':' + minutes  + ':' + seconds;
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
                LastLogin = LastLogin.replace('argument', id );
                $.ajax({
                    type : "PUT",
                    url : LastLogin,
                    data: {
                        "last_login" : dateString + 'T'+ timeString + 'Z',
                        'csrfmiddlewaretoken': csrf
                    }
                });
                window.location.href = "/home";
            }
        },
        error : function(){
            alert(get_url);
        }
    });
}
function logout(){
    sessionStorage.removeItem("user_id"); // keyName에 해당하는 값 삭제
    sessionStorage.removeItem("password"); // keyName에 해당하는 값 삭제
}
$(document).ready(function(){
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
});