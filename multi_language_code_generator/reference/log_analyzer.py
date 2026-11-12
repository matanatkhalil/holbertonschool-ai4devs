class LogAnalyzer:
    def analyze(self, lines: list[str]) -> dict:
        requests_by_method = {}
        requests_by_status = {}
        endpoint_counts = {}
        total_response_time = 0
        total_requests = 0
        malformed_entries = 0
        errors = 0

        for line in lines:
            try:
                parts = line.split()

                if len(parts) != 5:
                    raise ValueError("Invalid log format")

                timestamp, method, endpoint, status, response_time = parts

                status = int(status)
                response_time = float(response_time)

                if not timestamp.endswith("Z") and "T" not in timestamp:
                    raise ValueError("Invalid timestamp")

                if not method.isalpha() or not endpoint.startswith("/"):
                    raise ValueError("Invalid method or endpoint")

                if not 100 <= status <= 599:
                    raise ValueError("Invalid status code")

                if response_time < 0:
                    raise ValueError("Invalid response time")

                # Count valid requests
                total_requests += 1
                requests_by_method[method] = (
                    requests_by_method.get(method, 0) + 1
                )
                requests_by_status[str(status)] = (
                    requests_by_status.get(str(status), 0) + 1
                )
                endpoint_counts[endpoint] = (
                    endpoint_counts.get(endpoint, 0) + 1
                )

                total_response_time += response_time

                if status >= 400:
                    errors += 1

            except (ValueError, TypeError):
                malformed_entries += 1

        error_rate = (
            round(errors / total_requests * 100, 2)
            if total_requests else 0
        )

        average_response_time = (
            round(total_response_time / total_requests, 2)
            if total_requests else 0
        )

        most_requested_endpoint = (
            min(
                endpoint_counts,
                key=lambda endpoint: (-endpoint_counts[endpoint], endpoint)
            )
            if endpoint_counts else None
        )

        return {
            "totalRequests": total_requests,
            "requestsByMethod": requests_by_method,
            "requestsByStatus": requests_by_status,
            "errorRate": error_rate,
            "mostRequestedEndpoint": most_requested_endpoint,
            "averageResponseTime": average_response_time,
            "malformedEntries": malformed_entries
        }
