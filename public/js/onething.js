/* onething JS */
$(document).ready(function() {
    // Keep some hover history, so we can selectively reload
    var lastHover;

    $.each($(".opening em"), function(){
        $(this).hover(function(event){
            closestEm = $(event.target).closest("em").length;
            if (!$(".popover").length && closestEm) {
                $(this).popover({
                    animation: true,
                    placement: 'bottom'
                }).popover("show");
            } else if ($(".popover").length && closestEm) {
                if (lastHover.id != this.id) {
                    $("em").popover("destroy");
                    $(this).popover({
                        animation: true,
                        placement: 'bottom'
                    }).popover("show");
                }
            }
        lastHover = this;
        },function(event){
        });
        $(".wrapper").click(function(event) {
            if (!$(event.target).closest("em").length) {
                $('em').popover("destroy");
            };
        });
    });
});
