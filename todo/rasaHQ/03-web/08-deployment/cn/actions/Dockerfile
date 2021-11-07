FROM rasa/rasa-sdk:2.8.2

# The Rasa SDK image runs as non-root user by default. Hence, you have to switch
# back to the `root` user if you want to install additional dependencies
USER root

# WORKDIR /actions

# COPY . /actions
# RUN pip3 install --user --upgrade --no-warn-script-location pip

# RUN pip3 install --user --no-cache-dir -r requirements.txt
RUN pip3 install recognizers-text-suite

RUN pip3 install pandas
# Switch back to a non-root user
USER 1001


# CMD ["run", "actions"]