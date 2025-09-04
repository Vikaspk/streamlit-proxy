# Use a lightweight Nginx image
FROM nginx:alpine

# Copy our custom config
COPY nginx.conf /etc/nginx/nginx.conf

# Expose Railway's expected port
EXPOSE 8080

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
