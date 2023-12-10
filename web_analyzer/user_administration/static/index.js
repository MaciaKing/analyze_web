/*
function login(){
    var password = document.getElementById("passw");
    var email = document.getElementById("gmail");
    console.log("email:",email.value , "password:", password.value);
}

function createUser(email, password) {
    var users = jQuery.ajax({
        type: 'POST',
        url: 'localhost/',
        dataType:"json",
        data: {
            dat: "getAllUsr"
        },
        success: function (data) {
            showUsers(JSON.parse(data));
        },
        error: function (xhr, status, error) {
            var err = eval("(" + xhr.responseText + ")");
            alert(err.Message);
        }
    });
}
*/