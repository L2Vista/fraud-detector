# L2Vista Fraud Detector

The L2Vista Fraud Detector is a component designed to enhance the security of the L2Vista platform by detecting potential phishing addresses.
This component utilizes a list of known phishing addresses to proactively identify and mitigate potential risks.

## Getting Started

To run the L2Vista Fraud Detector, follow these steps:

1. Install the required dependencies using `pip`:

   ```bash
   $ pip install Flask flask-cors pandas
   ```

2. Clone this repository or download the provided code to your local machine.

3. Prepare the phishing address data:

   Place the phishing address data in a CSV file named `phishing-address.csv` in the same directory as the provided code. The CSV file should have a single column with the header "address", containing the list of phishing addresses.

   > The current phishing address list consists of real-world phishing addresses on Ethereum.

4. Run the fraud detector using the provided code:

   ```bash
   $ gunicorn -w 1 -b 0.0.0.0:30328 flask_server:app
   ```

## Usage

Once the fraud detector is up and running, you can interact with it using HTTP POST requests. Here's an example using `curl`:

```bash
$ curl -X POST -H "Content-Type: application/json" \
-d '{
    "lists_of_addresses": [
        ["0x0061fb5485dff4bb85c078dca80d19119224d97e", "0x002f0c8119c16d310342d869ca8bf6ace34d9c39"],
        ["0x993706A4fc0bBB2dDC10984562d174A51326bbcD", "0x0059b14e35dab1b4eee1e2926c7a5660da66f747"]
    ]
}' \
http://0.0.0.0:30328/check
```

This example demonstrates how to send addresses to the fraud detector for checking. The response will indicate whether the each address is found in the list of known phishing addresses or not.

## Example Response

The fraud detector's response will provide information about whether the each address is found in the list of known phishing addresses. Here's an example response:

```json
{"results":["phishing","phishing"]}
```
