<h2>CompanyFinder</h2>

This program utilizes a REST API to query macaddress.io. Upon a successful API call,
it parses the json file and produces the company name associated with the user
provided MAC address.

<h3>How to Run</h3>

```python3 CompanyFinder.py <MACADDRESS>```

Some possible MAC addresses to use:
  * 000017	Oracle
  * 00003D	AT&T
  * 001A11	Google, Inc.
  
  <h2>NOTES</h2>
  * I hardcoded my own API key for this iteration because I could not think of a way to provide
  appropriate access without it. Would need to add security protocols to hide API key as well as
  possibly throttling to avoid overuse.
