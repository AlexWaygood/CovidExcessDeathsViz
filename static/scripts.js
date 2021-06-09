function WhileLoading(){
    $('.content').hide();
    $('#loading').show();
    document.body.style.cursor = 'wait';
}

function TwitterShare(){
    var title = document.querySelector("meta[property='og:title']").getAttribute("content");
    window.open("https://twitter.com/intent/tweet?text=" + title + "&url=" + window.location.href + "&via=CovidGraph");
}

function FacebookShare(){
    window.open("https://www.facebook.com/sharer/sharer.php?u=" + window.location.href);
}

function LinkedInShare(){
    window.open("https://www.linkedin.com/shareArticle?mini-true&url=" + window.location.href);
}

function CopyLinkToClipboard(){
    navigator.clipboard.writeText(window.location.href);
}

function AddSocialShareLinks(){
    document.getElementById("twitter_icon").addEventListener("click", TwitterShare);
    document.getElementById("facebook_icon").addEventListener("click", FacebookShare);
    document.getElementById("linkedin_icon").addEventListener("click", LinkedInShare);
    document.getElementById("clipboard_copy_icon").addEventListener("click", CopyLinkToClipboard);
}

function LoadingCursor(){
    document.body.style.cursor = 'wait';
    return true;
}