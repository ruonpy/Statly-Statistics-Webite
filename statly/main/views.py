from django.views.generic import FormView
from .forms import NumberForm
from collections import Counter
import statistics
class CalculateStatistics(FormView):
    template_name="main.html"
    form_class=NumberForm
    success_url="/"
    def form_valid(self, form):
        numbers_str=form.cleaned_data["numbers"]
        numbers_list=list(map(int, numbers_str.split()))
        mode=Counter(numbers_list).most_common(1)[0][0]
        median=statistics.median(numbers_list)
        mean=sum(numbers_list)/len(numbers_list)
        span=max(numbers_list)-min(numbers_list)
        numbers_list.sort()
        lq = numbers_list[:len(numbers_list) // 2]
        uq = numbers_list[len(numbers_list) // 2:]
        q1 = statistics.median(lq)
        q3 = statistics.median(uq)
        iqr = q3 - q1
        
        result = {
            "mode": mode,
            "median": median,
            "mean": mean,
            "span": span,
            "lq": lq,
            "uq": uq,
            "iqr": iqr,
            "numbers": numbers_list
        }

        return self.render_to_response(self.get_context_data(form=form, result=result))
        