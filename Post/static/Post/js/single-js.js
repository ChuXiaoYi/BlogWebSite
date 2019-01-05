(function (window, document) {

    var layout   = document.getElementById('layout'),
        menu     = document.getElementById('menu'),
        menuLink = document.getElementById('menuLink'),
        content  = document.getElementById('main');

    function toggleClass(element, className) {
        var classes = element.className.split(/\s+/),
            length = classes.length,
            i = 0;

        for(; i < length; i++) {
          if (classes[i] === className) {
            classes.splice(i, 1);
            break;
          }
        }
        // The className is not found
        if (length === classes.length) {
            classes.push(className);
        }

        element.className = classes.join(' ');
    }

    function toggleAll(e) {
        var active = 'active';

        e.preventDefault();
        toggleClass(layout, active);
        toggleClass(menu, active);
        toggleClass(menuLink, active);
    }

    menuLink.onclick = function (e) {
        toggleAll(e);
    };

    content.onclick = function(e) {
        if (menu.className.indexOf('active') !== -1) {
            toggleAll(e);
        }
    };

}(this, this.document));

/*
鼠标滑过，显示回复功能
 */
function show_reply() {
    var reply = document.getElementById('reply');
    reply.style.display = 'inline';
}

/*
鼠标移开，隐藏回复功能
 */
function hidden_replay() {
    var reply = document.getElementById('reply');
    reply.style.display = 'none'
}

/*
点击"回复"，出现回复评论框
 */
function show_replyform(){
    var reply_form = document.getElementById('reply-form')
    reply_form.style.display = 'block';
}