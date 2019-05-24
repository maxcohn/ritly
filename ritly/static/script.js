
function sendLink(url, data){
    fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers:{
          'Content-Type': 'application/json'
        }
    })
}

$(document).ready(function(){
    $("#send").click(function(){
        console.log('Sending POST');
        var data = {
            link: $("#input").val(),
        };

		// check if any text is empty
        if(data.link === ''){
			alert('Link cannot be empty');
        	return;
        }

        var validURL = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/i
        
        if(!validURL.test(data.link)){
            alert('The entered link is not valid');
            return;
        }
    
        fetch('/new', {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers:{
              'Content-Type': 'application/json'
            }
        });
    });
});
