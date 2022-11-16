class FileUpload {
    constructor(input) {
        this.input = input
        this.max_length = 1024 * 1024 * 10; // 10 mb
    }

    upload() {
        this.create_progress_bar();
        this.initFileUpload();
    }

initFileUpload() {
    this.file = this.input.files[0];
    this.upload_file(0, null);
}

(function ($) {
    $('#submit').on('click', (event) => {
        event.preventDefault();
        var uploader = new FileUpload(document.querySelector('#fileupload'))
        uploader.upload();
    });
})(jQuery);
upload_file(start, path) {
    var end;
    var self = this;
    var existingPath = path;
    var formData = new FormData();
    var nextChunk = start + this.max_length + 1;
    var currentChunk = this.file.slice(start, nextChunk);
    var uploadedChunk = start + currentChunk.size
    if (uploadedChunk >= this.file.size) {
        end = 1;
    } else {
        end = 0;
    }
    formData.append('file', currentChunk);
    formData.append('filename', this.file.name);
    formData.append('end', end);
    formData.append('existingPath', existingPath);
    formData.append('nextSlice', nextChunk);
    $('.filename').text(this.file.name)
    $('.textbox').text("Uploading file")
    $.ajaxSetup({
    // make sure to send the header
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        xhr: function () {
            var xhr = new XMLHttpRequest();
            xhr.upload.addEventListener('progress', function (e) {
                if (e.lengthComputable) {
                    if (self.file.size < self.max_length) {
                        var percent = Math.round((e.loaded / e.total) * 100);
                    } else {
                        var percent = Math.round((uploadedChunk / self.file.size) * 100);
                    }
                    $('.progress-bar').css('width', percent + '%')
                    $('.progress-bar').text(percent + '%')
                }
            });
            return xhr;
        },

        url: "{%url 'library:file'%}",
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: {
            file:$("#fileupload").val()
        },
        error: function (xhr) {
            alert(xhr.statusText);
        },
        success: function (res) {
            if (nextChunk < self.file.size) {
                // upload file in chunks
                existingPath = res.existingPath
                self.upload_file(nextChunk, existingPath);
            } else {
                // upload complete
                $('.textbox').text(res.data);
                alert(res.data)
            }
        }
    });
};
create_progress_bar() {
    var progress = `<div class="file-icon">
                        <i class="fa fa-file-o" aria-hidden="true"></i>
                    </div>
                    <div class="file-details">
                        <p class="filename"></p>
                        <small class="textbox"></small>
                        <div class="progress" style="margin-top: 5px;">
                            <div class="progress-bar bg-success" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                            </div>
                        </div>
                    </div>`
    document.getElementById('uploaded_files').innerHTML = progress
}