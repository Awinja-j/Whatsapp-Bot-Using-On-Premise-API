# WhatsApp Bot

## Sample WhatsApp bot using python and WhatsApp on-premise API


The WhatsApp Business Platform gives medium to large businesses the ability to connect with customers at scale. You can start conversations with customers in minutes, send customer care notifications or purchase updates, offer your customers a level of personalized service and provide support in the channel that your customers prefer to be reached on.

Cloud API: Send and receive messages using a cloud-hosted version of the WhatsApp Business Platform.

On-Premises API: Your business can host the WhatsApp Business API client on your own servers using the On-Premises API.

Business Management API: The WhatsApp Business Management API allows you to programmatically manage your WhatsApp Business Account assets, such as message templates and phone numbers.

Before You Start:

ensure you have 
- A [Facebook Business Manager account](https://developers.facebook.com/micro_site/url/?click_from_context_menu=true&country=KE&destination=https%3A%2F%2Fbusiness.facebook.com%2F&event_type=click&last_nav_impression_id=07WSgb1ev5SLOS8xb&max_percent_page_viewed=32&max_viewport_height_px=821&max_viewport_width_px=1440&orig_http_referrer=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fwhatsapp%2Fon-premises%2Fget-started&orig_request_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fajax%2Fdocs%2Fnav%2F%3Fpath1%3Dwhatsapp%26path2%3Don-premises%26path3%3Dget-started&region=emea&scrolled=true&session_id=02p7AbgqM4AUosz6J&site=developers)
- A [verified business](https://developers.facebook.com/micro_site/url/?click_from_context_menu=true&country=KE&destination=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F2058515294227817&event_type=click&last_nav_impression_id=07WSgb1ev5SLOS8xb&max_percent_page_viewed=32&max_viewport_height_px=821&max_viewport_width_px=1440&orig_http_referrer=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fwhatsapp%2Fon-premises%2Fget-started&orig_request_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fajax%2Fdocs%2Fnav%2F%3Fpath1%3Dwhatsapp%26path2%3Don-premises%26path3%3Dget-started&region=emea&scrolled=true&session_id=02p7AbgqM4AUosz6J&site=developers)

- A [WhatsApp business account](https://developers.facebook.com/micro_site/url/?click_from_context_menu=true&country=KE&destination=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F2087193751603668&event_type=click&last_nav_impression_id=07WSgb1ev5SLOS8xb&max_percent_page_viewed=32&max_viewport_height_px=821&max_viewport_width_px=1440&orig_http_referrer=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fwhatsapp%2Fon-premises%2Fget-started&orig_request_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fajax%2Fdocs%2Fnav%2F%3Fpath1%3Dwhatsapp%26path2%3Don-premises%26path3%3Dget-started&region=emea&scrolled=true&session_id=02p7AbgqM4AUosz6J&site=developers)

- A Line of Credit for your WhatsApp business account — You can refer to [About WhatsApp Business API Billing](https://developers.facebook.com/micro_site/url/?click_from_context_menu=true&country=KE&destination=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F2225184664363779&event_type=click&last_nav_impression_id=07WSgb1ev5SLOS8xb&max_percent_page_viewed=32&max_viewport_height_px=821&max_viewport_width_px=1440&orig_http_referrer=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fwhatsapp%2Fon-premises%2Fget-started&orig_request_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fajax%2Fdocs%2Fnav%2F%3Fpath1%3Dwhatsapp%26path2%3Don-premises%26path3%3Dget-started&region=emea&scrolled=true&session_id=02p7AbgqM4AUosz6J&site=developers) for more information about the billing process as well.

- A command line tool such as Terminal or an app like Postman that can perform cURL requests.


## Getting started

Getting started with WhatsApp

1. Prepare assets




Getting started with this project

1. clone repo

```
git clone www.repo.com
```

2. install env

```
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt
```