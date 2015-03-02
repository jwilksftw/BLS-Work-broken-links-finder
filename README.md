# BLS-Work-broken-links-finder
Before I made this program, there was no way to check to see if any of the over 2,000 links in the 
Occupational Outlook Handbook (http://www.bls.gov/ooh) had broken/changed/404'd. 

This program runs in 2 parts. The first part pulls all of the external links from the publication and stores their 
addresses. The second part, which must be uncommented before use, will then check each link and see if an error is
returned. The output can then be used to change or remove any offending links.
