from aiohttp.web import Response
from aiohttp.web import View
from aiohttp_jinja2 import render_template

import numpy as np
import os


class IndexView(View):
    async def get(self) -> Response:
        return render_template("index_my.html", self.request, {})

    async def post(self) -> Response:
        try:
            form = await self.request.post()
            string = [form["request"]]
            model = self.request.app["model"]
            clf, transformer = model.clf, model.transformer
            a = transformer.transform(np.array(string).astype('U')).toarray()
            answer = clf.predict(a.reshape(-1, 1, 7711))[0][0]
            ctx = {"sent":string, "accuracy": round(answer, 3), "accuracy_str": str(round(100* answer, 2)) +'%'}
            return render_template("index_my.html", self.request, ctx)
        except Exception as err:
            ctx = {"error": str(err)}
            return render_template("index_my.html", self.request, ctx)
