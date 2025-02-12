# Use an Nginx image to serve static files
FROM nginx:latest

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy frontend files
COPY frontend /usr/share/nginx/html

# Expose the default Nginx HTTP port
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]