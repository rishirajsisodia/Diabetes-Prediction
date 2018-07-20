$(".counter").each(function() {
  var $this = $(this),
    countTo = $this.attr("data-count");
  if (countTo > 50) {
    $("body").css("background-color", "#B03A2E");
    $(".counter").css("background-color", "#943126");
    document.getElementById("paste").innerHTML = "RISKY!";
  } else if (countTo == 50) {
    $("body").css("background-color", "#ff8b90");
    $(".counter").css("background-color", "#ff7688");
    document.getElementById("paste").innerHTML = "Marginal";
  }

  $({ countNum: $this.text() }).animate(
    {
      countNum: countTo
    },

    {
      duration: 1000,
      easing: "linear",
      step: function() {
        $this.text(Math.floor(this.countNum));
      },
      complete: function() {
        $this.text(this.countNum);
        //alert('finished');
      }
    }
  );
});