document.addEventListener('DOMContentLoaded', () => {
    const thumbnails = document.querySelectorAll('.thumbnail');
    thumbnails.forEach(thumbnail => {
      thumbnail.addEventListener('mouseover', () => {
        console.log(thumbnail.dataset.videoId)
        const videoId = thumbnail.dataset.videoId;
        console.log(videoId)
        const videoEmbed = document.getElementById(videoId);
        if (videoEmbed) {
          thumbnail.classList.remove('thumbnail')
          thumbnail.style.display = 'none';
          videoEmbed.style.display = 'initial';
          const videoUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
          videoEmbed.insertAdjacentHTML('beforeend', `<iframe width="480" height="360" src="${videoUrl}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>`);
        } else {
          console.log(`Could not find videoEmbed element with id ${videoId}`);
        }
      });
    });
  });