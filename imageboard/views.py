from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.http import HttpResponseForbidden
from django.views import generic
from .models import Thread, Reply
from django.contrib.sessions.models import Session
from .forms import ThreadForm, ReplyForm


class ThreadListView(generic.ListView):
    model = Thread
    context_object_name = 'threads'
    paginate_by = 15


class ThreadCreateView(generic.CreateView):
    model = Thread
    form_class = ThreadForm

    def form_valid(self, form):
        form.instance.session_key = self.request.session.session_key
        return super().form_valid(form)


class ThreadEditView(generic.UpdateView):
    model = Thread
    template = 'thread_edit_form.html'
    fields = ['subject', 'comment']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.session_key != request.session.session_key:
            return HttpResponseForbidden()
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.session_key != request.session.session_key:
            return HttpResponseForbidden()
        return super().post(self, request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.session_key = self.request.session.session_key
        return super().form_valid(form)


def thread_delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if thread.session_key != request.session.session_key:
        return HttpResponseForbidden()
    if request.method == 'POST':
        thread.delete()
        return redirect('home')
    return redirect(thread)


class ReplyEditView(generic.UpdateView):
    model = Reply
    template = 'imageboard/reply_form.html'
    fields = ['comment']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.session_key != request.session.session_key:
            return HttpResponseForbidden()
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.session_key != request.session.session_key:
            return HttpResponseForbidden()
        return super().post(self, request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.session_key = self.request.session.session_key
        return super().form_valid(form)

    def get_object(self):
        self.thread = get_object_or_404(Thread, pk=self.kwargs["pk"])
        return get_object_or_404(Reply, pk=self.kwargs["reply_id"], thread=self.thread)


def reply_delete(request, pk, reply_id):
    thread = get_object_or_404(Thread, pk=pk)
    reply = get_object_or_404(Reply, pk=reply_id, thread=thread)
    if reply.session_key != request.session.session_key:
        return HttpResponseForbidden()
    if request.method == 'POST':
        reply.delete()
        return redirect(thread)
    return redirect(thread)


def thread_detail(request, pk):
    template = 'imageboard/thread_detail.html'
    thread = get_object_or_404(Thread, pk=pk)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = thread
            reply.session_key = request.session.session_key
            reply.save()
            return redirect(thread)
    else:
        form = ReplyForm()

    context = {
        'form': form,
        'thread': thread
    }
    return render(request, template, context)
