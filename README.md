# Language Translator

This is a Python project which, with the help of Google Translator, returns the translated language and also recognizes the text image to be translated.

## Project Overview

Read the full detailed synopsis of this project [here](https://docs.google.com/document/d/1XMYHRkkI5JIAnpCr1znKA9wqxsfcNGjSpEypLr8BgO0/edit?usp=drivesdk).

## Image Gallery

<div style="width: 80%; margin: 0 auto;">
  <style>
    .carousel {
      display: flex;
      overflow: hidden;
      width: 100%;
      margin: 20px 0;
    }
    .carousel img {
      width: 100%;
      flex-shrink: 0;
      transition: transform 0.5s ease;
    }
    .carousel-container {
      display: flex;
      position: relative;
      width: 100%;
      height: 0;
      padding-bottom: 75%; /* Aspect ratio 4:3 */
    }
    .carousel-inner {
      display: flex;
      width: 100%;
      transition: transform 0.5s ease;
    }
    .arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background-color: rgba(255, 255, 255, 0.7);
      border: none;
      padding: 10px;
      cursor: pointer;
    }
    .left-arrow {
      left: 10px;
    }
    .right-arrow {
      right: 10px;
    }
  </style>

  <div class="carousel">
    <button class="arrow left-arrow" onclick="moveSlide(-1)">&#10094;</button>
    <div class="carousel-container">
      <div id="carousel-inner" class="carousel-inner">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/e9a4fb91-25e6-4c26-bc7e-a67be6cb67b0" alt="Image 1">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/7027a4ef-6bb7-44cf-b8a6-1310eab5d519" alt="Image 2">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/b9a02cae-4020-4263-aa06-4548f9aadc34" alt="Image 3">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/96b6e057-498a-475e-8843-33d8de36c39a" alt="Image 4">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/9a464d04-b73c-48e1-bc35-7f6e3a70b178" alt="Image 5">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/8a73638f-e557-4b99-9d50-b9f8bf932c91" alt="Image 6">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/70b7bb0a-f6e7-47e8-8f9e-e63fe8a0b669" alt="Image 7">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/c8de6778-9768-458d-9472-f98d9b1e5a29" alt="Image 8">
        <img src="https://github.com/Chaitanya2238/Language_Translator/assets/122593924/551bf0b5-a4f1-4e81-9f67-7a0b55ce3366" alt="Image 9">
      </div>
    </div>
    <button class="arrow right-arrow" onclick="moveSlide(1)">&#10095;</button>
  </div>

  <script>
    let slideIndex = 0;

    function moveSlide(n) {
      const slides = document.querySelectorAll(".carousel img");
      slideIndex = (slideIndex + n + slides.length) % slides.length;
      const offset = -slideIndex * 100;
      document.getElementById("carousel-inner").style.transform = `translateX(${offset}%)`;
    }
  </script>
</div>

## Usage

1. Clone the repository
2. Install the required dependencies
3. Run the project




