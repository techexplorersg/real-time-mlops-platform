
```text
                   Training Pipeline
                          │
                          ▼
                    Model Candidate
                          │
                          ▼
                   Offline Evaluation
                          │
                          ▼
                     Registry
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
             Champion          Challenger
                 │                 │
                 └────────┬────────┘
                          ▼
                    Inference API
                          │
                          ▼
                 Feature Validation
                          │
                          ▼
                    Prediction
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          Latency       Errors       Features
             │            │            │
             └────────────┼────────────┘
                          ▼
                      Monitoring
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
             Data Drift      Model Metrics
                 │                 │
                 └────────┬────────┘
                          ▼
                  Promotion Policy
                          │
                    ┌─────┴─────┐
                    ▼           ▼
                 PROMOTE      REJECT
```

