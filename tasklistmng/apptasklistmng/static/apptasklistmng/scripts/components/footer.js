class Footer extends HTMLElement {
    constructor() {
        super();
    }


    connectedCallback() {
        this.innerHTML = `
        <footer style="text-align: center;color: #494040; clear:both">
            <p style="padding-top:30px">Go back to <a href="https://yuz876.github.io/Homepage/">my homepage</a> or <a href="https://github.com/yuz876">my Github Repos.</a></p>
            <p style="padding-top:30px">Copyright 2022 by Yujie Zhang. All Rights Reserved.</p>
        </footer>  
        `;
    }
}

customElements.define('footer-component', Footer);