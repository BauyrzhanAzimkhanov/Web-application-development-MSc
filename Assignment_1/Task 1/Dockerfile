FROM python AS initial_stage
COPY ./app.py .

FROM python:slim AS running_stage
COPY --from=initial_stage /app.py .
ENTRYPOINT [ "python", "app.py" ] 
