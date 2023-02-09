// Convert image data to base64 by image url

function convertImageToBase64(imgUrl, callback) {
	const image = new Image();
	image.crossOrigin='anonymous';
	image.onload = () => {
		const canvas = document.createElement('canvas');
		const ctx = canvas.getContext('2d');
		canvas.height = image.naturalHeight;
		canvas.width = image.naturalWidth;
		ctx.drawImage(image, 0, 0);
		const dataUrl = canvas.toDataURL();
		callback && callback(dataUrl)
	}
	image.src = imgUrl;
}


// Convert image selected from local to base64

const $file = document.querySelector(".local");
$file.addEventListener("change", (event) => {
	const selectedfile = event.target.files;
	if (selectedfile.length > 0) {
		const [imageFile] = selectedfile;
		const fileReader = new FileReader();
		fileReader.onload = () => {
			const srcData = fileReader.result;
			console.log('base64:', srcData)
		};
		fileReader.readAsDataURL(imageFile);
	}
});


// Convert clipboard’s image data to base64

async function parseClipboardImageData() {
  const items = await navigator.clipboard.read()
  for (let item of items) {
    for (let type of item.types) {
      if (type.startsWith("image/")) {
        return item
          .getType(type)
          .then(blob => {
            return new Promise((resolve) => {
              const fileReader = new FileReader();
              fileReader.onload = () => {
                const srcData = fileReader.result;
                resolve(srcData);
              };
              fileReader.readAsDataURL(blob);
            })
          })
      }
    }
  }
}