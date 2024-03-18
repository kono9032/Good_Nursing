function create_id() {
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');
    var r_pw = document.querySelector('#r_pw');

    if(id.value == "" || pw.value == "" || r_pw.value == "") {
        alert("회원가입을 할 수 없습니다.")    
    }
    else {
        if(pw.value !== r_pw.value) {
            alert("비밀번호를 확인해주세요.")
        }
        else {
            var form = document.createElement("form");
            form.setAttribute("charset", "UTF-8");
            form.setAttribute("method", "Post");  //Post 방식
            form.setAttribute("action", "../create_id"); //요청 보낼 주소

            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", "id_");
            hiddenField.setAttribute("value", id.value);
            form.appendChild(hiddenField);

            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", "pw_");
            hiddenField.setAttribute("value", pw.value);
            form.appendChild(hiddenField);

            document.body.appendChild(form);
            form.submit();
        }
    }
}
    
function join() {location.href = "join"}
function back() {history.go(-1);}

function roadtable(value){
    var rfid = $(value).text();
    var form = document.createElement("form");
    form.setAttribute("charset", "UTF-8");
    form.setAttribute("method", "Post");  //Post 방식
    form.setAttribute("action", "/loading"); //요청 보낼 주소

    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", "RFID");
    hiddenField.setAttribute("value", rfid);
    form.appendChild(hiddenField);

    document.body.appendChild(form);
    form.submit();
}