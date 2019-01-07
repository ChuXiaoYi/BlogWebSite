(function (window, document) {

    var layout = document.getElementById('layout'),
        menu = document.getElementById('menu'),
        menuLink = document.getElementById('menuLink'),
        content = document.getElementById('main');

    function toggleClass(element, className) {
        var classes = element.className.split(/\s+/),
            length = classes.length,
            i = 0;

        for (; i < length; i++) {
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

    content.onclick = function (e) {
        if (menu.className.indexOf('active') !== -1) {
            toggleAll(e);
        }
    };

}(this, this.document));


/**
 * 鼠标滑过，显示回复功能
 */
function show_reply(obj) {
    obj.getElementsByClassName('reply')[0].style.display = 'inline-block';
}

/**
 * 鼠标移开，隐藏回复功能
 */
function hidden_replay(obj) {
    obj.getElementsByClassName('reply')[0].style.display = 'none';
}

/**
 * 点击"回复"，出现回复评论框
 */
function show_replyform(obj) {
    obj.parentElement.getElementsByClassName('reply-form')[0].style.display = 'block';
    obj.parentElement.getElementsByClassName('comment-content')[0].focus();
    // obj.parentElement.getElementsByClassName('comment-div')[0].getElementsByClassName('pure-button')[0]
    //     .setAttribute("id", "text-focus-on")
}

/**
 * 评论失焦自动隐藏
 */
function hidden_replyform(obj) {
    //todo
    // obj.parentElement.style.display = 'none';
}

/**
 * 评论区聚焦的时候，出现昵称、邮箱的表单
 */
function show_person_info(obj){
    obj.parentElement.getElementsByClassName('pure-group')[0].style.display = 'block'
}
