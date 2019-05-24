
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
        // Valid URL formats:
        // http://www.website.com
        // www.website.com
        // http://website.com

        // regex for valid urls
        var validURL = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/i
        
        if(!validURL.test(data.link)){
            alert('The entered link is not valid');
            return;
        }
        
        // check if the given link begins with 'http://' or now
        if(data.link[0] === 'w'){
            // the given link doesn't begin with the protocol, so we add it in
            data.link = "http://" + data.link;
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
