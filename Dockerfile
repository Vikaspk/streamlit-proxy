FROM nginx:alpine

# Copy config and substitute env vars (Railway provides PORT)
COPY nginx.conf /etc/nginx/templates/default.conf.template

EXPOSE 8080

CMD ["sh", "-c", "envsubst < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
