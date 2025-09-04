FROM nginx:alpine

# Install envsubst
RUN apk add --no-cache gettext

# Copy template config
COPY nginx.conf.template /etc/nginx/templates/default.conf.template

EXPOSE 8080

# Substitute $PORT and start nginx
CMD ["/bin/sh", "-c", "envsubst < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
