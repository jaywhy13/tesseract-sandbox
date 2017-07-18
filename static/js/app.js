var app = new Vue({
  el: '#app',
  data: {
    imageId: null,
    processedImageUrl: null,
    processOperation: null,
    extractedText: "Hello",
  },
  methods: {
    processImage: function(){
        var vm = this;
        if(this.processOperation){
            console.log("Processing image");
            var url = "/process_image/" + this.imageId + "/" + this.processOperation;
            $.get(url).then(function(data){
                if(data.image){
                    console.log("Setting processed image url");
                    vm.processedImageUrl = "/uploads/" + data.image;
                    vm.extractedText = data.text
                }
            });
        }
   
    }
  }

})