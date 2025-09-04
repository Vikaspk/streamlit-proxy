FROM nginx:alpine

# envsubst for port injection
RUN apk add --no-cache gettext

# Put template where we can substitute $PORT safely
COPY nginx.conf.template /etc/nginx/templates/default.conf.template

EXPOSE 8080

# Substitute ONLY $PORT so Nginx variables like $http_upgrade remain intact
CMD ["/bin/sh", "-c", "envsubst '$PORT' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
