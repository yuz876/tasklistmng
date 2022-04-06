class Header extends HTMLElement{
    constructor(){
        super();
    }

    connectedCallback(){
        this.innerHTML = `
        <header>
            <a href="index.html">Home</a>
            <a href="signin.html">Sign In</a> 
            <a href="signon.html">Sign On</a> 
            <a href="https://yuz876.github.io/Homepage/">My Homepage</a>
        </header>

        `;
    }
}
customElements.define('header-component', Header);

