// ==UserScript==
// @name        weibo-mini
// @namespace    https://github.com/Hansimov
// @description   Publish weibo everywhere.
// @author      Hansimov
// @version     0.1
// @match       https://www.google.com.hk/*
// @match       https://www.baidu.com/*
// @grant       GM_getValue
// @grant       GM_setValue
// @grant      GM_addStyle
// @run-at     document-end
// @updateURL    https://github.com/Hansimov/weibo-mini/weibo-mini.user.js
// @require     https://code.jquery.com/jquery-3.3.1.min.js
// ==/UserScript==

(function() {
    'use strict';
    console.log("Hello, this is weibo-mini! 1501");
    var $ = window.jQuery;
    var newHTML = document.createElement ('div');
    newHTML.innerHTML = '<div id="test-div" style="background-color:powderblue; font-family:Consolas Bold; font-weight:bold;" align="center">This is my test div!</div>';
    document.body.appendChild(newHTML);
    GM_addStyle('#test-div { font-size: 40px; top:80px; position:fixed; z-index:120;}');
})();