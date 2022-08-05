function clickevent(){
    var user_id = document.getElementById('id').value;
    var password = document.getElementById('password').value;
    var re_password = document.getElementById('re_password').value;

    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2);
    var day = ('0' + today.getDate()).slice(-2);
    var dateString = year + '-' + month  + '-' + day;

    var hours = ('0' + today.getHours()).slice(-2); 
    var minutes = ('0' + today.getMinutes()).slice(-2);
    var seconds = ('0' + today.getSeconds()).slice(-2); 
    var timeString = hours + ':' + minutes  + ':' + seconds;
    if(user_id == undefined || user_id == ''){
        alert("아이디를 입력하세요");
    }
    else if (password == undefined){
        alert("비밀번호를 입력해주세요");
    }
    else if (re_password == undefined){
        alert("비밀번호 확인을 입력해주세요");
    }
    else if(password != re_password){
        alert("비밀번호와 비밀번호 확인이 다릅니다.");
    }
    else{
        $.ajax({
            type : "GET",
            url : get_url,
            success : function(data){
                var flag = 0;
                for(var i = 0;i<data.length;i++){
                    if(data[i]['user_id'] == user_id){
                        flag = 1;
                    }
                }
                if (flag == 0){
                    $.ajax({
                        type: "POST",
                        url: post_url,
                        data: {
                            "user_id" : user_id,
                            "password" : password,
                            "date" : dateString + 'T'+ timeString + 'Z',
                            'csrfmiddlewaretoken': csrf
                        },
                        dataType: "json",
                        success: function() {
                            location.href("../home");
                        },
                    });
                    alert("회원가입 완료");
                    window.location.href = "../home";
                }
                else{
                    alert("이미 존재하는 아이디입니다.");
                    window.location.href = "/sign_up";
                }
            },
            error : function(){
                alert("error");
            }
        });
    }
}