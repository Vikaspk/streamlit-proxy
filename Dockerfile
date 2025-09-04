FROM nginx:alpine

# Copy config into conf.d (not main nginx.conf!)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
