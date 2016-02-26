$(document).ready(function() {

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
}
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });

    function updateCounter(element, count, liked) {
        element.html(count)
        if (liked == true) {
            element.removeClass('picto__heart-empty')
            element.addClass('picto__heart-full')
        } else {
            element.addClass('picto__heart-empty')
            element.removeClass('picto__heart-full')
        }
    }

    $('.project__counter').click(function(){
        that = $(this)
        var project = that.data('project');
        if (project != undefined) {
            $.ajax({
                type: "POST",
                url: '/vote/',
                data: {"project_id": project},
                success: function(data, status) { updateCounter(that, data['count'], data['liked']) },
                error: updateCounter,
                dataType: 'json'
            })
        }
});

});
