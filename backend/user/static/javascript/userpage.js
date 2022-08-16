$(document).ready(function(){
    login_ck = $(".navbar_menu");
    seetion_user_id = sessionStorage.getItem("user_id")
    seetion_password = sessionStorage.getItem("password")
    if (seetion_user_id != null){
        login_ck.append(`<li><a href = "../userpage">UserPage</a></li>`);
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
            if (flag != 1){
                var title = $('div.item_title');
                title.append(`<a class = "profile_button" href ="../write">Profile</a>`);
                // window.location.href = "/write"
            }
            else{
                var nickname = $('div.nickname');
                var email = $('div.email');
                var PhoneNumber = $('div.PhoneNumber');
                var Identity_Verification = $('div.Identity_Verification');
                var Api_key = $('div.Api_key');
                var Sec_key = $('div.Sec_key');
                var Password = $('div.Password');
                var lastlogin = $('div.Login');

                var login_data = data[idx]['last_login'].replace('Z','').replace('T',' ');
                
                nickname.append(`<span class="Nickname">`+ data[idx]['nickname'] +`</span>`);
                lastlogin.append(`<span class="Login">`+ login_data +`</span>`);
                email.append(`<span class="Nickname">`+ data[idx]['Email'] + `</span>`);
                PhoneNumber.append(`<span class="Phone">`+ data[idx]['phone_number'] +`</span>`);
                Identity_Verification.append(`<span class="Identity">`+ data[idx]['Identity_Verification'] +`</span>`)
                Password.append(`<span class="Password">`+ data[idx]['password'] +`</span>`)
                Api_key.append(`<span class="api_key">`+ data[idx]['api_key'] +`</span>`)
                Sec_key.append(`<span class="sec_key">`+ data[idx]['sec_key'] +`</span>`)
            }
        },
        error : function(){
            alert(get_url);
        }
    });
    
});