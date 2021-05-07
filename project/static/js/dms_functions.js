window.onload = function()
{
    scrollBottom();
}

function showCreate()
{
    var formItems = [...document.getElementsByClassName('create-form-popup')];
    var background = document.getElementById("dimmer");
    for (var i = 0; i < formItems.length; i++)
    {
        formItems[i].style.display = "block";
    }
    background.style.display = "block";
}

function hideCreate()
{
    var formItems = [...document.getElementsByClassName('create-form-popup')];
    var background = document.getElementById("dimmer");
    for (var i = 0; i < formItems.length; i++)
    {
        formItems[i].style.display = "none";
    }
    background.style.display = "none";
}

function showChats(className)
{
    var messages = [...document.getElementById('message-text').children];
    for (var i = 0; i < messages.length; i++)
    {
        if (messages[i].className == className)
        {
            messages[i].style.display = "block";
        }
        else
        {
            messages[i].style.display = "none";
        }
    }
    scrollBottom();
}

function scrollBottom()
{
    var scrollDiv = [...document.getElementsByClassName('message-text')][0];
    scrollDiv.scrollTop = scrollDiv.scrollHeight;
}

function getChatMessage()
{
    var messages = [...document.getElementById('message-text').children];
    for (var i = 0; i < messages.length; i++)
    {
        if (messages[i].style.display == "block")
        {
            $.post( "/dm", {
                class_name: messages[i].className
            });
        }
    }
}