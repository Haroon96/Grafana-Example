# Grafana-Example

The example contains 3 Docker containers, one for a Flask app, one for a Prometheus instance, and one for a Grafana instance.
1. Start the docker containers using `docker compose up --build`.
2. Start the web app by opening `http://localhost:9001` in your browser. The app provides one metric value called `api_counter` that we'll plot inside Grafana. This value can be changed by pressing the Increment and Decrement buttons in the app.
3. Prometheus should now be running as well and pointed to the web app (see prometheus/config.yaml).
4. Open the Grafana instance by opening `http://localhost:3000` in your browser. The username and password is `admin` and `admin`. Once logged in, you'll see the Grafana interface. From the left menu bar, click on `Dashboards` and then `New dashboard`. 
5. Click `Add visualization` and then `Configure a new data source`.
6. In the new tab, select `Prometheus` and under the `Prometheus server URL`, enter `http://prometheus:9090`. Scroll to the bottom and click `Save & test` and it should show success.
7. Go back to the create dashboard tab and refresh. Click `Add visualization` again and select the Prometheus data source.
8. The add panel screen will show up. Under `Query`, click on the `Select metric` drop-down and look for the `api_counter` metric which was added from the web app.
9. Under Options, you can edit the graph visuals.
10. On the right, set the panel title to whatever you want.
11. Click `Save` on the top and enter the dashboard title.
12. You'll now land on the Dashboard for your metrics.
13. Click the three dots next to the plot and go to `View`. On the top-right, you'll see a dropdown for the time set to last 6 hours. Change it to last 5 minutes.
14. In the web app, press the Increment and Decrement buttons to change the metric value.
15. The updated metric values will appear in Grafana as time passes.
16. Repeat steps 7-12 to add all the metrics for your app.

## Custom Metrics
Inside the web app, `app.py` line 10 has a `api_counter` gauge created. You can register as many gauges for your app and all of these would show up in Grafana.