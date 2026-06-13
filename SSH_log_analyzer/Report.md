# Report : SSH logs alaysis
Analysis of the SSH log file revealed several security alerts.

A total of 59 failed login attempts occurred over a period of approximately 57 minutes, an average rate of about one attempt per minute.

The analysis shows that four IP addresses were responsible for these unsuccessful login attempts:

* 45.77.12.9
* 203.0.113.50
* 198.51.100.22
* 185.44.10.7

These IP addresses targeted the following accounts:

* root: 42 attempts
* admin: 11 attempts
* guest: 4 attempts
* test: 2 attempts

No successful logins were observed for these accounts during the period covered by the log file.

The 59 failed login attempts targeted the server1 server via the SSH2 protocol.

## Conclusion and Recommendations

The four identified IP addresses should be further investigated to determine if they are involved in malicious activity. If their malicious nature is confirmed, blocking them at the firewall level should be considered.

Although no successful connections from these IP addresses were observed in the analyzed logs, it is recommended to check the targeted accounts as a precaution:

* root
* admin
* guest
* test

The logs show no signs of limiting connection attempts during the observed period. It is recommended to verify the presence and configuration of protection mechanisms against brute-force attacks, such as Fail2ban, account lockout after multiple failed authentication attempts, retry limiting, or multi-factor authentication (MFA).

The observed behavior is consistent with a brute-force attack attempt targeting the SSH service.