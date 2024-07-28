SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

*/2 * * * * pg_dump -U postgres spike > /dumps/spike_dump.sql
