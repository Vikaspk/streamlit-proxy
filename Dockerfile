FROM nginx:alpine

# envsubst for $PORT only
RUN apk add --no-cache gettext

# use a template so $PORT is substituted but Nginx vars ($http_upgrade, etc.) remain intact
COPY nginx.conf.template /etc/nginx/templates/default.conf.template

EXPOSE 8080

# substitute ONLY $PORT, then start nginx
CMD ["/bin/sh", "-c", "envsubst '$PORT' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
