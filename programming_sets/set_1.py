def savings(gross_pay, tax_rate, expenses):
    post_taxes = int(gross_pay * (1 - tax_rate))  # floor the value
    return post_taxes - expenses

def material_waste(total_material, material_units, num_jobs, job_consumption):
    q = total_material - (job_consumption * num_jobs)
    return f"{q}{material_units}"

def interest(principal, rate, periods):
    interest = principal * (rate * periods)
    return int(principal + interest)
