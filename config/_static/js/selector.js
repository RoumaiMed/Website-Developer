$(function() {
    window.gotoProduct = function(product) {
        var urlArr = window.location.href.split('/');
        urlArr[urlArr.length - 2] = 'latest';
        urlArr[urlArr.length - 3] = product;
        window.location.href = urlArr.join('/');
    }
    window.gotoVersion = function(version) {
        var urlArr = window.location.href.split('/');
        urlArr[urlArr.length - 2] = version;
        window.location.href = urlArr.join('/');
    }
    const selectors = document.querySelectorAll('.target-selector');
    const productSelector = selectors[0];
    const versionSelector = selectors[1];
    productSelector.addEventListener('change', function() {
        window.gotoProduct(this.value);
    });
    versionSelector.addEventListener('change', function() {
        window.gotoVersion(this.value);
    });
})
