console.log('Check script!')


// Get Stripe publishable key
fetch("/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
        // Initialize Stripe.js
        const stripe = Stripe(data.publicKey);
        const itemId = document.URL.split('/').pop()
        const button = document.getElementById('submitBtn')
        const hostName = document.location.origin
        const url = hostName + '/buy/' + itemId
        // Get Stripe publishable key
        button.addEventListener("click", () => {
            // Get Checkout Session ID
            fetch(url, {
                method: 'GET',
                itemId: itemId,
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (session) {
                    return stripe.redirectToCheckout({ sessionId: session.id });
                })
                .then(function (result) {
                    // If `redirectToCheckout` fails due to a browser or network
                    // error, you should display the localized error message to your
                    // customer using `error.message`.
                    if (result.error) {
                        alert(result.error.message);
                    }
                });
        });
    });

